<template>
  <div class="h-auto pb-1 box-border border-neutral-500 border rounded-md px-2">
    <div
      class="
        text-neutral-600
        font-semibold
        px-0
        w-full
        whitespace-no-wrap
        rounded
        transition
        duration-300
        focus:outline-none
        cursor-pointer
        flex
        justify-between
      "
      @click="show = !show"
    >
      <span>
        {{ navElementName }}
      </span>
      <span :class="{ 'transform rotate-180 ': show }" class="w-auto">
        <svg
          class="h-8 w-8 text-gray-600"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </span>
    </div>
    <div
      class="
        top-20
        block
        left-0
        m-0
        pt-1
        w-full
        leading-5
        align-baseline
        bg-scroll
        text-black
      "
      v-if="show"
    >
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Collapsible",
  emits: ["activateCollapsible"],
  props: {
    navElementName: {
      type: String,
      required: true,
    },
  },
  data: function () {
    return {
      show: false,
    };
  },
  watch: {
    show(value) {
      if (value == true) {
        this.$emit("activateCollapsible");
      }
    },
  },
};
</script>

<style scoped>
</style>