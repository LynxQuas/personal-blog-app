<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  visible: { type: Boolean, required: true },
  isDeleting: Boolean,
});

const emit = defineEmits(["confirm", "cancel"]);
</script>

<template>
  <transition name="fade">
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black/40 z-50">
      <div
        class="bg-white rounded-2xl shadow-xl w-[90%] max-w-sm p-6 flex flex-col gap-4 text-center animate-scale"
      >
        <h2 class="text-lg font-semibold text-gray-800">Delete Confirmation</h2>
        <p class="text-gray-600 text-sm">
          Are you sure you want to delete this item? This action cannot be undone.
        </p>

        <div class="flex justify-center gap-4 mt-4">
          <button
            @click="emit('cancel')"
            class="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 text-gray-700"
          >
            Cancel
          </button>

          <button
            @click="emit('confirm')"
            class="px-4 py-2 rounded-lg bg-red-500 hover:bg-red-600 text-white"
          >
            {{ isDeleting ? "Deleting" : " Yes, Delete" }}
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<style scoped>
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
