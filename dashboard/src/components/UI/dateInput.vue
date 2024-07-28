<template>
  <div>
    <div
      :class="{
        empty:
          this.modelValue === '' || this.modelValue === null ? true : false,
        'mb-10': alertEmpty,
         'relative h-10 mb-5':
            hasBorder,
      }"
    >
      <input
        :class="{
          'ring-red-400': alertEmpty,
          'border border-neutral-400 rounded-md focus:ring-1 focus:ring-main-600 focus:outline-none':
            hasBorder,
          'border border-transparent rounded-md': !hasBorder,
        }"
        :id="id"
        :ref="id"
        :required="required ? true : false"
        type="date"
        :value="modelValue"
        :min="(minvalue ? minvalue :'')"
        :max="(maxvalue ? maxvalue :'')"
        @blur="CheckIfAlert($event)"
        @input="InputValue($event)"
        :readonly="readonly ? true : false"
        class="h-full w-full 2xl:px-2 md:px-0 transition-all rounded-sm bg-transparent md:text-xs 2xl:text-lg"
        list="list"
      />
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
  name: "date-input-float",
  model: {
    prop: "modelValue",
    event: "update",
  },
  props: {
    modelValue: {
      type: String,
      default: null,
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
      required: false,
    },
    maxvalue: {
      required: false,
    },
    hasBorder: {
      type: Boolean,
      required: false,
      default: true,
    },
    required: {
      type: Boolean,
      default: false,
    },
    readonly: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["update:modelValue"],
  data() {
    return {
      id: `input-${
        Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)
      }`,
      alertEmpty: false,
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
    InputValue(event) {
      this.$emit("update:modelValue", event.target.value || null);
    },
    CheckIfAlert(event) {
      this.alertEmpty =
        event.target.value == "" && this.required ? true : false;
    },
  },
};
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
input[type="number"] {
  -moz-appearance: textfield;
}
</style>