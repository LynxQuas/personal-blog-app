<script setup>
import { useAuthStore } from "@/stores/auth";
import { LucideChevronDown, LucideLogOut, LucidePen, LucideUser } from "lucide-vue-next";
import { onMounted, onUnmounted, ref } from "vue";
import { useRouter } from "vue-router";

const showDropdown = ref(false);
const router = useRouter();

const auth = useAuthStore();

const handleLogout = () => {
  auth.logout();
  router.push("/");
};

const closeDropdown = (event) => {
  const dropdown = document.getElementById("user-dropdown");
  if (dropdown && !dropdown.contains(event.target)) showDropdown.value = false;
};

onMounted(() => document.addEventListener("click", closeDropdown));
onUnmounted(() => document.removeEventListener("click", closeDropdown));
</script>

<template>
  <div v-if="auth.currentUser" class="relative" id="user-dropdown">
    <button class="flex items-center gap-2" @click.stop="showDropdown = !showDropdown">
      <LucideUser />
      <span>{{ auth.currentUser.username }}</span>
      <LucideChevronDown
        :class="`transition-transform duration-200 ${showDropdown ? 'rotate-180' : ''}`"
      />
    </button>

    <transition name="fade">
      <div
        v-if="showDropdown"
        class="absolute bg-navBg right-0 mt-3 w-40 rounded-xl shadow-lg py-2"
      >
        <RouterLink
          to="/admin/create"
          class="flex items-center gap-2 px-4 py-2"
          @click="showDropdown = false"
        >
          <LucidePen size="16" />
          <span>Create Blog</span>
        </RouterLink>

        <button class="flex items-center gap-2 px-4 py-2 w-full text-left" @click="handleLogout">
          <LucideLogOut size="16" />
          <span>Logout</span>
        </button>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
