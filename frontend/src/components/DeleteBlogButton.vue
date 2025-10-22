<script setup>
import { ref } from "vue";
import DeleteConfirmModal from "@/components/DeleteConfirmModal.vue";
import { useRouter } from "vue-router";
import { deleteBlog } from "@/libs/https";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const showDeleteModal = ref(false);
const isDeleting = ref(false);
const props = defineProps({
  blog_id: Number,
});

const auth = useAuthStore();

const deleteItem = async () => {
  isDeleting.value = true;
  try {
    const data = await deleteBlog(props.blog_id, auth.token);
    router.push("/blogs");
  } catch (err) {
    console.log(err);
  } finally {
    isDeleting.value = false;
  }
};
</script>

<template>
  <button
    class="bg-red-500 text-white px-4 py-2 rounded-lg"
    @click.stop.prevent="showDeleteModal = true"
  >
    Delete
  </button>

  <DeleteConfirmModal
    :visible="showDeleteModal"
    @confirm="deleteItem"
    @cancel="showDeleteModal = false"
    :isDeleting="isDeleting"
  />
</template>
