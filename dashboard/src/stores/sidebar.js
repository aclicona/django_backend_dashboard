import { defineStore } from 'pinia';

export const useSidebarStore = defineStore('sidebar', {
  state: () => ({
    sideBarOpen: true, // Example initial state
  }),
  getters: {
    isSideBarOpen: (state) => state.sideBarOpen,
  },
  actions: {
    toggleSidebar() {
      this.sideBarOpen = !this.sideBarOpen;
    },
  },
});