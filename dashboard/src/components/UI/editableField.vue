<template>
  <div>
    <div
      class="relative"
      :class="{
        empty:
          this.textareatext === '' || this.textareatext === null ? true : false,
        'mb-10': alertEmpty,
      }"
    >
      <div
        :class="(hasBorder ? 'border border-neutral-400 rounded-md' : 'border border-transparent rounded-md')"
        class="outline-none overflow-hidden overflow-y-auto focus:border-main-700 focus:border rounded-md px-2"
        contenteditable
        :ref="id"
        @blur="InputValue()"
      >{{textareatext}}</div>
      <label
        @click="$refs[id].focus()"
        class="
          select-none
          transform
          -translate-y-1/2
          top-0
          text-sm text-main-600
          absolute
          left-2
          transition-all
          bg-white
          px-1
          rounded-sm
        "
        v-bind:for="id"
      >
        <slot></slot>
      </label>
      <label class="text-red-400" v-if="alertEmpty">Campo requerido</label>
    </div>
  </div>
</template>

<script>
export default {
  name: "editable-field",
  props: {
    modelValue: {
      type: String,
    },
    tipo: {
      type: String,
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
    },
    hasBorder: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  emits: ["update:modelValue"],
  data() {
    return {
      id: `input-${
        Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)
      }`,
      // textareatext: this.modelValue,
      textareatext: null,
      alertEmpty: false,
      textAreaMaxHeight: 0,
      textareaInline: {
        maxHeight: "30vh",
        overflow: "hidden",
        height: "2.75rem",
      },
    };
  },
  computed: {
    type_exchange() {
      if (this.tipo === "number") {
        return "text";
      }
      return this.tipo;
    },
  },
  methods: {
    InputValue() {
      this.textareatext = this.$refs[this.id].innerText;
      if (this.tipo == "number") {
        this.textareatext = this.textareatext.replace(/\D/g, "");
        if (this.maxvalue && this.textareatext > this.maxvalue) {
          this.textareatext = this.maxvalue;
        }
      }
      if (this.list) {
        const filterByAttr = (listAttributes = [], name) => {
          return listAttributes.find((attribute) => attribute.name === name);
        };
        const result = filterByAttr(this.list, this.textareatext);
        if (result) {
          this.$emit("update:modelValue", result.name);
        } else {
          this.$emit("update:modelValue", null);
        }
      } else {
        this.$emit("update:modelValue", this.textareatext || null);
      }
    },
    CheckIfAlert(event) {
      this.alertEmpty =
        event.target.value == "" && this.required ? true : false;
    },
    formatJustNumber(event) {
      if (this.tipo == "number") {
        event.target.value = event.target.value.replace(/[^\d]/g, "");
      }
    },    
  },
  mounted() {
    this.textareatext = this.modelValue
  }
};
</script>

<style scoped>
.empty div:not(:focus) + label {
  top: 50%;
  transform: translateY(-50%);
  font-size: 14px;
}

div:not(:focus) + label {
  color: rgba(70, 70, 70, 1);
}

div::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

div[type="number"] {
  -moz-appearance: textfield;
}
</style>