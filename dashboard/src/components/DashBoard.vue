<template>
  <div class="leading-normal tracking-normal" id="main-body">
    <div class="flex flex-wrap min-h-screen">
      <side-bar />
      <div
        class="w-full bg-gray-100 pl-0 lg:pl-52 2xl:pl-64 min-h-screen relative"
        :class="sideBarState.visible ? 'overlay' : ''"
        id="main-content"
      >
        <nav-bar />
        <div class="p-3 2xl:p-5 bg-gray-100">
          <div id="alert-block"></div>
          <router-view />
        </div>
        <footer-bar />
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import FooterBar from '@/components/FooterBar.vue';
import { useSidebarStore } from '@/stores/sidebar'
import SideBar from '@/components/SideBar.vue'
const sideBarState = useSidebarStore()

</script>
