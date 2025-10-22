<script setup>
import { ref } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { LucideMenu, LucideX } from "lucide-vue-next";
import { useAuthStore } from "@/stores/auth";
import AdminDropDown from "./AdminDropDown.vue";
import MobileNavMenu from "./MobileNavMenu.vue";
import { NAV_MENU } from "@/constants/navlink";

const route = useRoute();
const auth = useAuthStore();

const showMobileNav = ref(false);

const isActiveLink = (path) => (path === "/" ? route.path === path : route.path.includes(path));
</script>

<template>
  <header
    class="py-4 lg:py-6 absolute top-0 left-0 w-full text-white bg-[#1F2937] z-20 backdrop-blur-md px-6 md:px-32 shadow-xs shadow-gray-300"
  >
    <nav class="flex w-full justify-between items-center relative">
      <RouterLink to="/" class="md:text-lg font-mono">PERSONAL BLOG APP</RouterLink>

      <!-- Desktop Nav -->
      <div class="hidden lg:flex items-center gap-x-20">
        <ul class="flex gap-6 items-center">
          <RouterLink
            v-for="menu in NAV_MENU"
            :key="menu.path"
            :to="menu.path"
            :class="`py-2 border-gray-100 ${isActiveLink(menu.path) ? 'text-activeNav' : ''}`"
          >
            {{ menu.label }}
          </RouterLink>
        </ul>

        <AdminDropDown />
      </div>

      <button class="lg:hidden" @click="showMobileNav = !showMobileNav">
        <LucideMenu v-if="!showMobileNav" />
        <LucideX v-else />
      </button>
    </nav>
  </header>

  <transition name="slide-fade">
    <MobileNavMenu v-if="showMobileNav" v-model:showMobileNav="showMobileNav" />
  </transition>
</template>

<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-fade-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}
.slide-fade-enter-to {
  opacity: 1;
  transform: translateY(0);
}
.slide-fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
