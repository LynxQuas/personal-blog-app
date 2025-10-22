<script setup>
import BlogLatestList from "@/components/BlogLatestList.vue";
</script>
<template>
  <section class="flex flex-col gap-y-10 w-full lg:w-[50rem] lg:m-auto text-wrap">
    <div class="mt-28">
      <h1 class="text-3xl font-bold text-center py-8">MY PERSONAL BLOG PAGE</h1>
      <p class="text-wrap text-gray-500 leading-6 tracking-wide">
        Hi there! I’m John Doe, and this is my personal space to share thoughts, ideas, and
        experiences on technology, travel, creativity. Here, you’ll find stories, guides, and
        reflections that inspire me—and hopefully spark some inspiration for you too. Grab a cup of
        coffee, explore, and make yourself at home!
      </p>
    </div>

    <div class="flex flex-col pb-10">
      <h2 class="text-xl font-semibold py-8">LATEST ARTICLES</h2>
      <BlogLatestList />
      <RouterLink class="text-blue-500 underline flex-end self-end" to="/blogs"
        >See more articles</RouterLink
      >
    </div>
  </section>
</template>
