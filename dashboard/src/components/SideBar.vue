
<!--      <router-link :to="{ name: 'CRWList' }" :class="-->
<!--        currentRouteName == 'CRWList' || currentRouteName == 'CRWDetail'-->
<!--          ? 'bg-main-700'-->
<!--          : 'hover:bg-gray-200'-->
<!--      " class="-->
<!--          w-full-->
<!--          flex-->
<!--          items-center-->
<!--          text-blue-400-->
<!--          h-7-->
<!--          xl:h-10-->
<!--          pl-4-->
<!--          rounded-->
<!--          cursor-pointer-->
<!--        " v-if="authorizedOption({groups:['Analista']})">-->
<!--        <svg :class="-->
<!--          currentRouteName == 'CRWList' || currentRouteName == 'CRWDetail'-->
<!--            ? 'text-white'-->
<!--            : 'text-main-700'-->
<!--        " class="h-5 w-5 xl:h-6 xl:w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"-->
<!--             stroke-linejoin="round">-->
<!--          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"-->
<!--                d="M17 14v6m-3-3h6M6 10h2a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v2a2 2 0 002 2zm10 0h2a2 2 0 002-2V6a2 2 0 00-2-2h-2a2 2 0 00-2 2v2a2 2 0 002 2zM6 20h2a2 2 0 002-2v-2a2 2 0 00-2-2H6a2 2 0 00-2 2v2a2 2 0 002 2z"/>-->
<!--        </svg>-->
<!--        <span :class="-->
<!--          currentRouteName == 'CRWList' || currentRouteName == 'CRWDetail'-->
<!--            ? 'text-white'-->
<!--            : 'text-main-700'-->
<!--        " class="pl-2 text-sm xl:text-base">Procesos</span>-->
<!--      </router-link>-->


<template>
  <div
    class="
      w-1/2
      md:w-1/3
      lg:w-52
      2xl:w-64
      fixed
      md:top-0 md:left-0
      h-screen
      min-h-screen
      lg:block
      bg-gray-100
      border-r
      z-30
    "
    :class="sideBarState.visible ? '' : 'hidden'"
    id="main-nav"
  >
    <div class="w-full h-14 2xl:h-16 border-b flex px-4 items-center justify-center mb-8 bg-gray-100">
      <p class="font-semibold text-2xl bg-gray-100 text-main-800 text-center">DASHBOARD</p>
    </div>

    <div class="mb-4 px-4">
      <p class="pl-4 text-sm font-semibold mb-1">MENÚ</p>
      <router-link
        :to="{ name: 'home' }"
        :class="currentRouteName === 'home' ? 'bg-main-700' : 'hover:bg-gray-200'"
        class="
          w-full
          flex
          items-center
          text-blue-400
          h-7
          xl:h-10
          pl-4
          rounded
          cursor-pointer
        "
      >
        <svg
          :class="currentRouteName === 'home' ? 'text-white' : 'text-main-700'"
          class="h-5 w-5 xl:h-6 xl:w-6"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path stroke="none" d="M0 0h24v24H0z" />
          <polyline points="5 12 3 12 12 3 21 12 19 12" />
          <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" />
          <rect x="10" y="12" width="4" height="4" />
        </svg>
        <span :class="currentRouteName === 'home' ? 'text-white' : 'text-main-700'" class="pl-2 text-sm xl:text-base">
          Dashboard
        </span>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useSidebarStore } from '../stores/sidebar';
import { useRoute } from 'vue-router';
// import Cookie from 'cookie-universal';


const route = useRoute();
// const router = useRouter();

const sideBarState = useSidebarStore();
const currentRouteName = computed(() => route.name);

// const authorizedByGroup = (authLevels = [], permisos = []) => {
//   if (authLevels) {
//     for (let group of authLevels) {
//       if (permisos.includes(group)) {
//         return true;
//       }
//     }
//     return false;
//   }
//   return false;
// };
//
// const authorizedOption = (option) => {
//   const cookies = Cookie();
//   const grupos = (cookies.get('userGroups') || '').split('.') || [];
//   const superUser = cookies.get('superUser') || false;
//   if (option.groups !== undefined && option.groups) {
//     const authorized = authorizedByGroup(option.groups, grupos);
//     return authorized || superUser;
//   }
//   return true;
// };
//
// const goToRoute = (routeName) => {
//   router.push({
//     name: routeName,
//   });
// };
</script>

<style scoped>
/* Add any styles if needed */
</style>