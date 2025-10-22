<script setup>
import "md-editor-v3/lib/style.css";
import { MdEditor } from "md-editor-v3";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import DisplayErrorModal from "@/components/DisplayErrorModal.vue";
import { createBlog } from "@/libs/https";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const isCreating = ref(false);
const auth = useAuthStore();

const state = reactive({
  title: "",
  description: "",
  content: "# Write your content here",
  image_url: "",
});

const modal = reactive({
  visible: false,
  message: [],
});

const onCreateBlog = async () => {
  isCreating.value = true;
  try {
    const data = await createBlog(state, auth.token);

    if (data?.detail) {
      modal.message = data.detail.map((err) => err.msg);
      modal.visible = true;
    } else {
      router.push(`/blogs/${data.id}`);
    }
  } catch (error) {
    console.error("Error creating blog:", error);
  } finally {
    isCreating.value = false;
  }
};
</script>
<template>
  <div class="mt-28 flex flex-col gap-y-5 flex-1 justify-center items-center self-center">
    <form @submit.prevent="onCreateBlog" class="w-full md:w-full lg:w-[70rem] p-4">
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

        <MdEditor v-model="state.content" :preview="false" height="700px" language="enUs" />

        <div class="flex justify-end">
          <button
            :disabled="isCreating"
            type="submit"
            class="bg-[#E07A5F] hover:bg-[#C86C55] text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transition-all"
          >
            {{ isCreating ? "Creating..." : "Create" }}
          </button>
        </div>
      </div>
    </form>

    <DisplayErrorModal v-model:visible="modal.visible" :msg="modal.message" />
  </div>
</template>

<style scoped>
:deep(.md-editor) {
  --md-bk-color: #f5f7fa !important; /* background color */
  --md-color: #333 !important; /* text color */
  --md-toolbar-bg-color: #fffdf6 !important;
  --md-border-color: #e0e0e0 !important;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.animate-scale {
  animation: scaleIn 0.15s ease;
}
@keyframes scaleIn {
  from {
    transform: scale(0.9);
    opacity: 0.7;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
