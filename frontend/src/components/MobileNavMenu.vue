<script setup>
import { useAuthStore } from "@/stores/auth";
import { useRoute, useRouter } from "vue-router";
import { LucideLogOut, LucidePen } from "lucide-vue-next";
import { NAV_MENU } from "@/constants/navlink";

const route = useRoute();
const router = useRouter();
const auth = useAuthStore();

const handleLogout = () => {
  auth.logout();
  router.push("/");
};

const props = defineProps({
  showMobileNav: Boolean,
});

const emit = defineEmits(["update:showMobileNav"]);

const onCloseMenu = () => {
  return emit("update:showMobileNav", false);
};
const isActiveLink = (path) => (path === "/" ? route.path === path : route.path.includes(path));
</script>

<template>
  <div
    class="lg:hidden z-20 absolute bg-navBg text-white w-full top-[6%] shadow-md rounded-b-xl py-4 px-6 flex flex-col gap-3"
  >
    <RouterLink
      v-for="menu in NAV_MENU"
      :key="menu.path"
      :to="menu.path"
      :class="`py-2 border-gray-100 ${isActiveLink(menu.path) ? 'text-activeNav' : ''}`"
      @click="onCloseMenu"
    >
      {{ menu.label }}
    </RouterLink>
    <div v-if="auth.currentUser" class="pt-3 border-t border-gray-200 flex flex-col gap-2">
      <RouterLink
        to="/admin/create"
        :class="`flex items-center gap-2 px-2 py-2  rounded-md ${
          isActiveLink('/admin/create') ? 'text-activeNav' : ''
        }`"
        @click="onCloseMenu"
      >
        <LucidePen size="16" />
        <span>Create Blog</span>
      </RouterLink>
      <button class="flex items-center gap-2 px-2 py-2 rounded-md text-left" @click="handleLogout">
        <LucideLogOut size="16" />
        <span>Logout</span>
      </button>
    </div>
  </div>
</template>

<!-- <style scoped>
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
</style> -->
