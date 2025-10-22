<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  total: { type: Number, required: true }, // total items
  perPage: { type: Number, default: 8 }, // items per page
});

const emit = defineEmits(["page-change"]);
const currentPage = ref(1);

const totalPages = computed(() => Math.ceil(props.total / props.perPage));

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
    emit("page-change", page);
  }
};
</script>

<template>
  <div class="flex items-center justify-center gap-2 mt-6">
    <button
      @click="goToPage(currentPage - 1)"
      :disabled="currentPage === 1"
      class="px-3 py-1 rounded-lg border text-sm hover:bg-gray-100 disabled:opacity-50"
    >
      Prev
    </button>

    <template v-for="page in totalPages" :key="page">
      <button
        @click="goToPage(page)"
        :class="[
          'px-3 py-1 rounded-lg border text-sm transition',
          currentPage === page
            ? 'bg-blue-600 text-white border-blue-600'
            : 'hover:bg-gray-100 border-gray-300',
        ]"
      >
        {{ page }}
      </button>
    </template>

    <button
      @click="goToPage(currentPage + 1)"
      :disabled="currentPage === totalPages"
      class="px-3 py-1 rounded-lg border text-sm hover:bg-gray-100 disabled:opacity-50"
    >
      Next
    </button>
  </div>
</template>
