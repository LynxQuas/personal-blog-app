<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import BlogList from "@/components/BlogList.vue";
import Pagination from "@/components/Pagination.vue";
import { getBlogs } from "@/libs/https";
import { Router } from "lucide-vue-next";

const searchQuery = ref("");
const sortMethod = ref("newest");
const blogs = ref([]);
const total = ref(0);
const page = ref(1);
const limit = ref(3);
const loading = ref(false);

const route = useRoute();
const router = useRouter();

const fetchBlogs = async () => {
  loading.value = true;

  const query = new URLSearchParams({
    q: searchQuery.value,
    sort: sortMethod.value,
    skip: (page.value - 1) * limit.value,
  }).toString();

  try {
    const data = await getBlogs(query);
    blogs.value = data.data;
    total.value = data.total;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
};

const updateQuery = () => {
  router.replace({
    query: {
      q: searchQuery.value || undefined,
      sort: sortMethod.value,
      page: page.value,
    },
  });
};

const onSearch = () => {
  page.value = 1;
  updateQuery();
};

const onPageChange = (newPage) => {
  page.value = newPage;
  updateQuery();
};

watch(sortMethod, () => {
  page.value = 1;
  updateQuery();
});

watch(
  () => route.query,
  () => {
    searchQuery.value = route.query.q || "";
    sortMethod.value = route.query.sort || "newest";
    page.value = Number(route.query.page) || 1;
    fetchBlogs();
  },
  { deep: true }
);

onMounted(() => {
  searchQuery.value = route.query.q || "";
  sortMethod.value = route.query.sort || "newest";
  page.value = Number(route.query.page) || 1;
  fetchBlogs();
});
</script>

<template>
  <div class="mt-28 flex flex-col items-center gap-y-4 pb-10">
    <div class="flex flex-col md:flex-row w-full gap-y-5 gap-x-4 md:w-[30rem]">
      <input
        type="search"
        v-model="searchQuery"
        placeholder="Search by title..."
        class="py-2 px-4 border w-full border-gray-400 rounded-md"
      />
      <div class="flex gap-x-4 items-center">
        <button @click="onSearch" class="bg-blue-500 text-white px-4 py-2 rounded-md">
          Search
        </button>
        <select
          v-model="sortMethod"
          class="p-2 rounded-lg border border-gray-300 bg-white shadow-md cursor-pointer"
        >
          <option value="newest">Newest</option>
          <option value="oldest">Oldest</option>
        </select>
        <RouterLink class="text-center" to="/blogs">reset</RouterLink>
      </div>
    </div>

    <BlogList :blogs="blogs" :loading="loading" />
    <Pagination :total="total" :perPage="limit" @page-change="onPageChange" />
  </div>
</template>
