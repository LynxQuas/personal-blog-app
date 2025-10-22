<script setup>
import { formatFullDate } from "@/utils";
import { RouterLink } from "vue-router";

const props = defineProps({
  id: Number,
  image: String,
  title: String,
  description: String,
  created_at: String,
  class: String,
  imgSize: String,
});
</script>
<template>
  <RouterLink :to="`/blogs/${id}`" :class="class">
    <img :class="`${imgSize} rounded-md`" :src="image" />
    <div class="flex flex-col gap-y-2">
      <h3 class="font-bold line-clamp-2">{{ title }}</h3>
      <p class="line-clamp-3 md:line-clamp-3 text-sm">
        {{ description }}
      </p>
      <span class="text-gray-400 text-xs">{{ formatFullDate(created_at) }}</span>
    </div>
  </RouterLink>
</template>
