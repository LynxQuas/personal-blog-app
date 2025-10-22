<script setup>
import { RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <Navbar />
  <main class="lg:px-32 px-4">
    <RouterView />
  </main>
</template>
