<script setup>
import BlogCard from "./BlogCard.vue";
defineProps({
  blogs: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
});
</script>

<template>
  <div class="flex flex-wrap justify-center py-20 gap-y-6 gap-x-4">
    <h2 v-if="loading">Loading...</h2>
    <template v-else>
      <BlogCard
        v-for="blog in blogs"
        :key="blog.id"
        :id="blog.id"
        :image="blog.image_url"
        :title="blog.title"
        :description="blog.description"
        :created_at="blog.created_at"
        imgSize="w-full h-40"
        class="flex gap-x-6 w-[20rem] flex-col shadow-md shadow-gray-300 p-4 hover:shadow-lg transition-all hover:translate-y-[-2px]"
      />
      <p v-if="!blogs.length">No blogs found.</p>
    </template>
  </div>
</template>
