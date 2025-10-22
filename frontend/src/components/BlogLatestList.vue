<script setup>
import { onMounted, reactive } from "vue";
import BlogCard from "./BlogCard.vue";
import { getLatestBlogs } from "@/libs/https";

const latestBlogs = reactive({
  data: [],
  isLoading: true,
  error: "",
});

onMounted(async () => {
  try {
    const data = await getLatestBlogs();
    latestBlogs.data = data;
  } catch (err) {
    latestBlogs.error = "Something went wrong.";
  } finally {
    latestBlogs.isLoading = false;
  }
});
</script>

<template>
  <div class="flex flex-col gap-y-8 pb-8">
    <h2 v-if="latestBlogs.isLoading">Loading....</h2>
    <BlogCard
      v-else
      v-for="blog in latestBlogs.data"
      :key="blog.id"
      :id="blog.id"
      class="flex gap-x-6 flex-col md:flex-row shadow-md bg-secondary shadow-gray-300 p-4 hover:shadow-lg transition-all hover:translate-y-[-2px]"
      :image="blog.image_url"
      :title="blog.title"
      imgSize="md:w-[20rem] h-[10rem] w-full"
      :description="blog.description"
      :created_at="blog.created_at"
    />
  </div>
</template>
