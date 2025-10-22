<script setup>
import { onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import "md-editor-v3/lib/style.css";
import { MdEditor } from "md-editor-v3";
import DisplayErrorModal from "@/components/DisplayErrorModal.vue";
import { getBlog, updateBlog } from "@/libs/https";
import { useAuthStore } from "@/stores/auth";

const auth = useAuthStore();
const route = useRoute();
const router = useRouter();
const isUpdating = ref(false);
const modal = reactive({
  visible: false,
  message: "",
});

const state = reactive({
  title: "",
  description: "",
  content: "",
  image_url: "",
});

const getBlogData = async (blog_id) => {
  try {
    const data = await getBlog(blog_id);
    Object.assign(state, data);
  } catch (error) {
    console.error("Error fetching blog:", error);
  }
};

const handleContentChange = (newContent) => {
  state.content = newContent;
};

const onUpdateBlog = async () => {
  try {
    const data = await updateBlog(route.params.id, state, auth.token);

    if (data?.detail) {
      modal.message = data.detail.map((err) => err.msg);
      modal.visible = true;
      return;
    }

    router.push(`/blogs/${data.id || route.params.id}`);
  } catch (error) {
    console.error("Error updating blog:", error);
  }
};

onMounted(() => getBlogData(route.params.id));
</script>

<template>
  <div class="mt-28 flex flex-col gap-y-5 flex-1 justify-center items-center self-center">
    <form @submit.prevent="onUpdateBlog" class="w-full md:w-full lg:w-[70rem] p-4">
      <div class="flex flex-1 flex-col gap-3 pb-10 shrink-1">
        <input
          type="text"
          name="title"
          class="py-2 px-8 border bg-inherit border-gray-400"
          placeholder="Blog Title"
          v-model="state.title"
        />

        <textarea
          name="description"
          id="description"
          rows="2"
          class="py-2 px-8 bg-inherit border border-gray-400"
          placeholder="Blog Description"
          v-model="state.description"
        ></textarea>

        <input
          type="text"
          placeholder="image url"
          v-model="state.image_url"
          class="py-2 px-8 border bg-inherit border-gray-400"
        />

        <MdEditor
          @change="handleContentChange"
          v-model="state.content"
          height="700px"
          language="enUs"
        />

        <div class="flex items-center gap-x-4 justify-end">
          <RouterLink :to="`/blogs/${route.params.id}`">Cancel</RouterLink>
          <button
            :disabled="isUpdating"
            type="submit"
            class="bg-[#E07A5F] hover:bg-[#C86C55] text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transition-all"
          >
            {{ isUpdating ? "Updating..." : "Update" }}
          </button>
        </div>
      </div>
    </form>

    <DisplayErrorModal v-model:visible="modal.visible" :msg="modal.message" />
  </div>
</template>

<style scoped>
:deep(.md-editor) {
  --md-bk-color: #f5f7fa !important;
  --md-color: #333 !important;
  --md-toolbar-bg-color: #fffdf6 !important;
  --md-border-color: #e0e0e0 !important;
}
</style>
