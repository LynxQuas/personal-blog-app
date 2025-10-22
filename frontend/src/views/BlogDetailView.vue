<script setup>
import { MdPreview } from "md-editor-v3";
import { onMounted, reactive } from "vue";
import { useRoute } from "vue-router";
import "md-editor-v3/lib/style.css";
import DeleteBlogButton from "@/components/DeleteBlogButton.vue";
import { getBlog } from "@/libs/https";
import { useAuthStore } from "@/stores/auth";

const route = useRoute();
const auth = useAuthStore();
const blogData = reactive({
  data: {},
  error: "",
  isLoading: true,
});

onMounted(async () => {
  try {
    const blog = await getBlog(route.params.id);
    blogData.data = blog;
  } catch (err) {
    console.log(err);
    blogData.error = "Something went wrong try again.";
  } finally {
    blogData.isLoading = false;
  }
});
</script>

<template>
  <section class="lg:my-6 lg:mx-10 pt-28 relative">
    <div class="flex flex-1 items-center justify-center">
      <div class="w-full md:w-[50rem] flex flex-col gap-y-4">
        <div v-if="auth.currentUser" class="flex items-center gap-x-4">
          <DeleteBlogButton :blog_id="blogData.data.id" />
          <RouterLink
            :to="`/admin/blogs/edit/${blogData.data.id}`"
            class="bg-blue-500 py-2 px-4 text-white rounded-md"
            >Edit</RouterLink
          >
        </div>
        <h2 class="text-center text-3xl font-semibold">{{ blogData.data.title }}</h2>
        <img
          class="object-cover max-h-80"
          :src="blogData.data.image_url"
          :alt="blogData.data.title"
        />
        <p>{{ blogData.data.description }}</p>
        <MdPreview language="enUs" :model-value="blogData.data.content" />
      </div>
    </div>
  </section>
</template>
<style scoped>
:deep(.md-editor) {
  --md-bk-color: #f5f7fa !important;
  --md-color: #333 !important;
  --md-toolbar-bg-color: #fffdf6 !important;
  --md-border-color: #e0e0e0 !important;
}
</style>
