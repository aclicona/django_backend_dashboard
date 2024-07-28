<template>
  <div>
    <label :for="id" class="inline-flex items-center cursor-pointer">
      <span class="relative">
        <span
          :class="
            currentState
              ? 'bg-main-100'
              : 'bg-gray-200'
          "
          class="block w-10 h-6 rounded-full shadow-inner"
        ></span>
        <span
          :class="
            currentState
              ? 'bg-main-400 transform translate-x-full'
              : 'bg-white'
          "
          class="
            absolute
            block
            w-4
            h-4
            mt-1
            ml-1
            rounded-full
            shadow
            inset-y-0
            left-0
            focus-within:shadow-outline
            transition-transform
            duration-300
            ease-in-out
          "
        >
          <input
            :id="id"
            type="checkbox"
            class="absolute opacity-0 w-0 h-0"
            model="currentState"
            @change="InputValue"
            @click="currentState = !currentState"
            :disabled="deshabilitado"
          />
        </span>
      </span>
      <span class="ml-3 text-sm">
        <slot></slot>
      </span>
    </label>
  </div>
</template>
<script>
export default {
  name: "toggle",
  model: {
    prop: "modelValue",
    event: "update",
  },
  props: {
    modelValue: {
      type: Boolean,
      default: false,
    },
    deshabilitado: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["update:modelValue", "toggled"],
  data() {
    return {
      id: `input-${
        Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)
      }`,
      currentState: this.modelValue,
    };
  },
  methods: {
    InputValue() {
      this.$emit("update:modelValue", this.currentState);
      this.$emit("toggled",);
    },
  },
};
</script>