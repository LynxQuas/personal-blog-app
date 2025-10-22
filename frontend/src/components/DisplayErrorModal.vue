<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  visible: Boolean,
  msg: {
    type: [Array, String],
    default: () => [],
  },
});

const emits = defineEmits(["update:visible"]);

const closeModal = () => {
  emits("update:visible", false);
};
</script>

<template>
  <transition name="fade">
    <div
      v-if="props.visible"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full animate-scale">
        <h2 class="text-lg font-bold mb-4">Try again</h2>
        <ul class="flex flex-col gap-2">
          <li v-for="(msg, index) in props.msg" :key="index" class="whitespace-pre-line">
            {{ msg.replace(/^Value error, /, "") }}
          </li>
        </ul>
        <div class="mt-4 flex justify-end">
          <button
            @click="closeModal"
            class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded"
          >
            Close
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
