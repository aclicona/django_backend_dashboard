<template>
    <div class="rounded border border-neutral-400 px-4 py-2">
        <label :for="id" :class="required && !FILE ? 'text-third-700' : 'text-neutral-700'"
               class="px-2 text-sm flex items-center">
            <span v-if="FILE" class="mr-2">
                <svg
                    class="h-6 w-6 text-main-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
            </span>
            <span v-else>Adjuntar:&nbsp;</span> {{ descripcion }}
        </label>
        <div class="flex items-center">
            <input type="file" title="Remover archivo"
                   :id="id" :ref="id" :accept="acceptType" @change="FileUpload" :required="required"
                   :class="{'file:bg-third-100 file:text-third-700 hover:file:bg-third-200':required && !FILE,
                'file:bg-neutral-200 file:text-neutral-700 hover:file:bg-neutral-300': !required && !FILE,
                'file:bg-main-400 file:text-main-700 hover:file:bg-main-300 bg-neutral-100': FILE}"
                   class="block w-auto text-sm text-neutral-500
                     file:mr-4 file:py-2 file:px-4
                     file:rounded-lg file:border-0
                     file:text-sm file:font-semibold"/>
            <span title="Remover archivo" v-if="FILE" @click="FileRemoved">
                <svg xmlns="http://www.w3.org/2000/svg"
                     class="h-6 w-6 text-red-500 cursor-pointer ml-3" viewBox="0 0 20 20"
                     fill="currentColor">
                <path fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                      clip-rule="evenodd"/>
                </svg>
            </span>

        </div>

    </div>
</template>

<script>
export default {
    name: "ArchivoAdjunto",
    emits: ["fileLoaded", "fileRemoved"],
    props: {
        descripcion: {
            type: String,
            required: true
        },
        required: {
            type: Boolean,
            required: false,
            default: false
        },
        acceptType: {
            type: String,
            required: false,
            default: "application/pdf"
        }
    },
    data() {
        return {
            id: `input-${Math.floor(Math.random() * 100000) + Math.floor(Math.random() * 10000)}`,
            FILE: null,
        }
    },
    methods: {
        FileUpload(event) {
            this.FILE = event.target.files[0];
            this.$emit("fileLoaded", this.descripcion, this.FILE);
        },
        FileRemoved() {
            this.FILE=null;
            this.$refs[this.id].value=''
            this.$emit("fileRemoved", this.descripcion);
        }
    }
}
</script>

<style scoped>
</style>