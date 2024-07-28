toggle.vue<template>
  <div :class="{
        'empty': (this.modelValue === '' || this.modelValue === null) ? true : false,
        'mb-10': alertEmpty
    }" class="group relative h-10 input-component">
    <input :class="{ 'border-pink-500': alertEmpty, 'border-neutral-400': !alertEmpty, 'bg-teal-100': readonly }"
           :id="id" :list="(list ? 'list-' + id : '')" :maxlength="maxlength" :name="name" :ref="id"
           :required="required ? true : false" :type="type_exchange" :value="modelValue" :readonly="readonly"

           @blur="CheckIfAlert($event)" @focusin="desformatearValor($event)" @focusout="formatearValor($event)" @input="InputValue($event)" class="px-3 py-2 bg-white border shadow-sm placeholder-slate-400 disabled:bg-slate-50
                    disabled:text-slate-500 disabled:border-slate-500 focus:outline-none
                    focus:border-main-600 focus:ring-main-600 block w-full rounded-sm sm:text-sm
                    focus:ring-0 focus:invalid:text-pink-600 focus:invalid:border-pink-500
                    focus:invalid:ring-pink-500 disabled:shadow-none"/>
    <label :class="modelValue ? 'text-main-500' : 'text-neutral-800'" @click="$refs[id].focus()"
           class="select-none transform -translate-y-1/2 w-fit top-0 text-sm absolute left-2 transition-all bg-white px-1 rounded-sm"
           v-bind:for="id">
      <slot></slot>
    </label>
    <label class="text-pink-500 text-sm" v-if="alertEmpty">Campo requerido</label>
    <datalist :id="'list-' + id" v-if="list">
      <option v-for="(element, index) in list" :key="'option-' + index">{{ element.name }}</option>
    </datalist>

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
    readonly: {
      type: Boolean,
      required: false,
      default: false
    },
    required: {
      type: Boolean,
      default: false
    },
    name: {
      type: String,
      required: false
    }
  },
  emits: ['update:modelValue'],
  data() {
    return {
      id: `input-${Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)}`,
      alertEmpty: false
    }
  },
  computed: {
    type_exchange() {
      if ((this.tipo === 'number') || (this.tipo === 'float')) {
        return 'number'
      }
      return this.tipo
    }
  },
  methods: {
    formatMoney(valor) {
      const formatterPeso = new Intl.NumberFormat("es-CO", {
        style: "currency",
        currency: "COP",
      });
      return formatterPeso.format(valor)
    },
    desformatearValor(event) {
      if (this.tipo == 'currency') {
        const numero_a = event.target.value.replace(/[$ .]/g, "").replace(',','.')
        event.target.value = numero_a
      }
    },
    formatearValor(event) {
      if (this.tipo == 'currency') {
        event.target.value = this.formatMoney(event.target.value)
      }
    },
    InputValue(event) {
      if (this.tipo == 'number') {
        if ((this.maxvalue) && (event.target.value > this.maxvalue)) {
          event.target.value = Number(this.maxvalue)
        }
      }
      if (this.tipo == 'float') {
        if ((this.maxvalue) && (event.target.value > this.maxvalue)) {
          event.target.value = Number(this.maxvalue)
        }
      }
      if (this.list) {
        const filterByAttr = (listAttributes = [], name) => {
          return listAttributes.find(attribute => attribute.name === name)
        }
        const result = filterByAttr(this.list, event.target.value)
        if (result) {
          this.$emit('update:modelValue', result.name);
        } else {
          this.$emit('update:modelValue', null);
        }
      } else {
        if ((this.tipo === 'number') || (this.tipo === 'float')) {
          this.$emit('update:modelValue', Number(event.target.value) || null);
        }
        this.$emit('update:modelValue', event.target.value || null);
      }
    },
    CheckIfAlert(event) {
      this.alertEmpty = ((event.target.value == "" && this.required) ? true : false)
    }
  },
  mounted() {
    if (this.tipo == 'float') {
      this.$refs[this.id].pattern = '[0-9.-]'
      this.$refs[this.id].step = 1 / 100
    } else if (this.tipo == 'number') {
      this.$refs[this.id].pattern = '[-0-9]'
      this.$refs[this.id].step = 1
    } else if (this.tipo == 'currency') {
      this.$refs[this.id].pattern = '[0-9.-]'
      this.$refs[this.id].step = 1 / 10
      this.$refs[this.id].value = this.formatMoney(this.$refs[this.id].value)
    }
  }
}
</script>

<style scoped>
.empty input:not(:focus) + label {
  @apply text-sm top-1/2 -translate-y-1/2 w-full max-w-inputlabel
}

input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type=number] {
  -moz-appearance: textfield;
}
</style>
