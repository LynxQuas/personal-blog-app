<script setup>
import { register } from "@/libs/https";
import { reactive } from "vue";
import { RouterLink, useRouter } from "vue-router";

const router = useRouter();

const registerData = reactive({
  userData: {
    username: "",
    password: "",
    confirmation: "",
  },
  error: "",
  isLoading: false,
});

const onInputChange = () => {
  registerData.error = "";
};

const onRegister = async () => {
  if (
    !registerData.userData.username ||
    !registerData.userData.password ||
    !registerData.userData.confirmation
  ) {
    registerData.error = "Fields must be filled.";
    return;
  } else if (registerData.userData.password !== registerData.userData.confirmation) {
    registerData.error = "Password do not match.";
    return;
  } else if (registerData.userData.password.length < 6) {
    registerData.error = "Password must be at least 6 characters.";
    return;
  } else if (registerData.userData.username.length < 6) {
    registerData.error = "Username must be at least 6 characters.";
    return;
  } else {
    registerData.isLoading = true;
    try {
      const data = await register(registerData.userData);
      if (data.detail) {
        registerData.error = data.detail;
        return;
      }
      router.push("/login");
    } catch (err) {
      console.log(err);
    } finally {
      registerData.isLoading = false;
    }
  }
};
</script>

<template>
  <section>
    <form @submit.prevent="onRegister" class="bg-white w-full">
      <div class="flex flex-1 flex-col gap-y-4 justify-center items-center min-h-screen">
        <h2 class="text-2xl font-semibold">Login</h2>
        <h2 class="text-red-500">{{ registerData.error && registerData.error }}</h2>
        <input
          type="text"
          name="name"
          v-on:change="onInputChange"
          class="py-4 px-4 border border-gray-400 w-[25rem] rounded-md"
          v-model="registerData.userData.username"
          placeholder="name"
        />
        <input
          type="password"
          name="password"
          class="py-4 px-4 border border-gray-400 w-[25rem] rounded-md"
          v-model="registerData.userData.password"
          placeholder="password"
        />
        <input
          type="password"
          name="confirmation"
          class="py-4 px-4 border border-gray-400 w-[25rem] rounded-md"
          v-model="registerData.userData.confirmation"
          placeholder="Confirm your password"
        />
        <div class="flex flex-end items-center justify-between gap-10">
          <button
            :disabled="registerData.isLoading"
            class="bg-blue-400 text-white font-semibold py-3 px-8 rounded-md"
          >
            Register
          </button>
          <RouterLink to="/login" class="underline text-blue-500">Login</RouterLink>
        </div>
      </div>
    </form>
  </section>
</template>
