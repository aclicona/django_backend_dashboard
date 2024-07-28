<template>
  <div>
    <label :for="id" class="inline-flex items-center">
      <span class="relative">
        <span
          :class="
            value
              ? 'bg-gray-100'
              : 'bg-gray-100'
          "
          class="block w-10 h-6 rounded-full shadow-inner"
        ></span>
        <span
          :class="
            value
              ? 'bg-gray-400 transform translate-x-full'
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
          <span
            :id="id"
            class="absolute opacity-0 w-0 h-0"
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
  name: "disabledToggle",
  props: {
    value: {
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
    };
  },
  methods: {

  },
};
</script>