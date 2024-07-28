<template>
    <div>
        <div :class="{'empty': (this.modelValue === '' || this.modelValue === null) ? true : false,
             'mb-10':alertEmpty}"
             class="relative h-10 input-component mb-5">
            <select
                    :class="{'ring-red-400':alertEmpty}"
                    :id="id"
                    :ref="id"
                    :value="modelValue"
                    @blur="CheckIfAlert($event)"
                    @change="InputValue($event)"
                    class="h-full w-full px-2 transition-all border border-main-600 rounded-sm text-main-600 focus:outline-none focus:ring-1 focus:ring-main-600"
            >
                <option v-for="(option, index) in list" :value="option.value" :key="index + option.value">{{option.name}}</option>
            </select>
            <label
                    @click="$refs[id].focus()"
                    class="select-none transform -translate-y-1/2 top-0  text-sm text-main-600 absolute left-2 transition-all bg-white px-1 rounded-sm"
                    v-bind:for="id">
                <slot></slot>
            </label>
            <label class="text-red-400" v-if="alertEmpty">Campo requerido</label>
        </div>

    </div>
</template>

<script>
    export default {
        name: "select-float",
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
                        return listAttributes.find(attribute => attribute.value === value)
                    }
                    const result= filterByAttr(this.list, event.target.value)
                    if (result) {
                        this.$emit('update:modelValue', result.value);
                    }else{
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
    .empty select:not(:focus) + label {
        top: 50%;
        transform: translateY(-50%);
        font-size: 14px;
    }
    select:not(:focus) + label {
        color: rgba(70, 70, 70, 1);
    }
</style>