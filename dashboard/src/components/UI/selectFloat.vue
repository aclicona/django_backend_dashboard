<template>
    <div>
        <div :class="{
            'empty': (this.modelValue === '' || this.modelValue === null),
            'mb-10': alertEmpty
        }" class="relative h-10 input-component">
            <select :class="alertEmpty ? 'border-pink-500' : 'border-neutral-400'" :id="id" :ref="id" :value="modelValue"
                @blur="CheckIfAlert($event)" @change="InputValue($event)" class="px-2 py-2 h-10 bg-white border shadow-sm placeholder-slate-400 disabled:bg-slate-50
                    disabled:text-slate-500 disabled:border-slate-500 focus:outline-none
                    focus:border-main-600 focus:ring-main-600 block w-full rounded-sm sm:text-sm
                    focus:ring-0 focus:invalid:text-pink-600 focus:invalid:border-pink-500
                    focus:invalid:ring-pink-500 disabled:shadow-none">
                <option :value="option.value" v-for="(option, index) in list" :key="'option-' + index">{{ option.name }}
                </option>
            </select>
            <label :class="modelValue ? 'text-main-500' : 'text-neutral-800'" @click="$refs[id].focus()"
                class="select-none transform -translate-y-1/2 top-0 text-sm absolute left-2 transition-all bg-white px-1 rounded-sm"
                v-bind:for="id">
                <slot></slot>
            </label>
            <div class="text-pink-500 text-sm" v-if="alertEmpty">Campo requerido</div>
        </div>
    </div>
</template>

<script>
export default {
    name: "select-float",
    model: {
        prop: 'modelValue',
        event: 'update'
    },
    props: {
        modelValue: {
            default: null
        },
        required: {
            type: Boolean,
            default: false
        },
        list: {
            type: Array,
            required: true,
        },
    },
    emits: ['update:modelValue'],
    data() {
        return {
            id: `input-${Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)}`,
            alertEmpty: false
        }
    },
    methods: {
        InputValue(event) {
            if (this.list) {
                const filterByAttr = (listAttributes = [], value) => {
                    return listAttributes.find(attribute => attribute.value == value)
                }
                const result = filterByAttr(this.list, event.target.value)
                if (result) {
                    this.$emit('update:modelValue', result.value);
                } else {
                    this.$emit('update:modelValue', null);
                }
            }
        },
        CheckIfAlert(event) {
            this.alertEmpty = ((event.target.value == "" && this.required) ? true : false)
        }
    },
}
</script>

<style scoped>
.empty select:not(:focus)+label {
    @apply text-sm top-1/2 -translate-y-1/2 w-10/12
}

.empty select:not(:focus)+label {
    @apply text-sm top-1/2 -translate-y-1/2
}
</style>