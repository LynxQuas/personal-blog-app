<script setup>
const API_URL = import.meta.env.VITE_API_URL;
import { reactive } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

const router = useRouter();

const userData = reactive({
  name: "",
  password: "",
});

const onLogin = async () => {
  try {
    const formBody = new URLSearchParams();
    formBody.append("username", userData.name);
    formBody.append("password", userData.password);

    const res = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formBody.toString(),
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Login failed");

    authStore.setToken(data.access_token);

    await authStore.fetchCurrentUser();
    if (authStore.currentSuer) {
      router.push("/");
    }
    router.push("/");
  } catch (err) {
    console.error(err.message);
  }
};
</script>

<template>
  <form @submit.prevent="onLogin" class="w-full">
    <div class="flex flex-1 flex-col gap-y-4 justify-center items-center min-h-screen">
      <h2 class="text-2xl font-semibold">Login</h2>
      <input
        type="text"
        class="py-4 px-4 border border-gray-400 w-full md:w-[25rem] rounded-md"
        v-model="userData.name"
        placeholder="name"
      />
      <input
        type="password"
        class="py-4 px-4 border border-gray-400 w-full md:w-[25rem] rounded-md"
        v-model="userData.password"
        placeholder="password"
      />
      <div class="flex flex-end items-center justify-between gap-10">
        <button class="bg-blue-400 text-white font-semibold py-3 px-8 rounded-md">Login</button>
        <RouterLink to="/register" class="underline text-blue-500"> Register </RouterLink>
      </div>
    </div>
  </form>
</template>
