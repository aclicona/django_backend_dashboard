<template>
  <div>
    <div :class="{'empty': (this.modelValue === '' || this.modelValue === null) ? true : false,
             'mb-10':alertEmpty}"
         class="relative h-10">
      <input
          :class="{'ring-red-400':alertEmpty}"
          :id="id"
          :maxlength="maxlength"
          :ref="id"
          :required="required ? true : false"
          :type="type_exchange"
          :value="modelValue"
          @blur="CheckIfAlert($event)"
          @input="InputValue($event)"
          class="h-full w-full px-2 transition-all rounded-sm text-main-600 border border-main-600 focus:outline-none focus:ring-1 focus:ring-main-600"
          :list="(list ? 'list-' + id:'')"
      />
      <label
          @click="$refs[id].focus()"
          class="select-none transform -translate-y-1/2 top-0  text-sm text-main-600 absolute left-2 transition-all bg-white px-1 rounded-sm"
          v-bind:for="id">
        <slot></slot>
      </label>
      <label class="text-red-400" v-if="alertEmpty">Campo requerido</label>
      <datalist :id="'list-' + id" v-if="list">
        <option v-for="(element, index) in list" :key="index+element.name">{{ element.name }}</option>
      </datalist>

    </div>

  </div>
</template>

<script>
export default {
  name: "input-float-label",
  model: {
    prop: 'modelValue',
    event: 'update'
  },
  props: {
    modelValue: {
      type: String,
      default: null
    },
    tipo: {
      type: String,
      default: 'text',
    },
    list: {
      type: Array,
      required: false,
    },
    maxlength: {
      type: Number,
      required: false,
    },
    minvalue: {
      type: Number,
      required: false,
    },
    maxvalue: {
      type: Number,
      required: false,
    },
    required: {
      type: Boolean,
      default: false
    }
  },
  emits: ['update:modelValue', 'setValue'],
  data() {
    return {
      id: `input-${Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)}`,
      alertEmpty: false
    }
  },
  computed: {
    type_exchange() {
      if (this.tipo === 'number') {
        return 'text'
      }
      return this.tipo
    }
  },
  methods: {
    InputValue(event) {
      if (this.tipo == 'number') {
        event.target.value = event.target.value.replace(/\D/g, '')
        if ((this.maxvalue) && (event.target.value > this.maxvalue)) {
          event.target.value = this.maxvalue
        }
      }
      if (this.list) {
        const filterByAttr = (listAttributes = [], name) => {
          return listAttributes.find(attribute => attribute.name === name)
        }
        const result = filterByAttr(this.list, event.target.value)
        if (result) {
          this.$emit('update:modelValue', result.name);
          this.$emit('setValue', result.value);
        } else {
          this.$emit('update:modelValue', null);
          this.$emit('setValue', null);
        }
      } else {
        this.$emit('update:modelValue', event.target.value || null);
      }
    },
    CheckIfAlert(event) {
      this.alertEmpty = ((event.target.value == "" && this.required) ? true : false)
    },
    formatJustNumber(event) {
      if (this.tipo == 'number') {
        event.target.value = event.target.value.replace(/[^\d]/g, '')
      }
    },
  },
}
</script>

<style scoped>
.empty input:not(:focus) + label {
  top: 50%;
  transform: translateY(-50%);
  font-size: 14px;
}

input:not(:focus) + label {
  color: rgba(70, 70, 70, 1);
}

input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type=number] {
  -moz-appearance: textfield;
}
</style>