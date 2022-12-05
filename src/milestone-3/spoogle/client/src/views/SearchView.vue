<script setup lang="ts">
import { inject, onBeforeMount, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import ResultList from "../components/ResultList.vue";
import FilterBox from "../components/FilterBox.vue";
import type { AxiosInstance } from "axios";
import { computed } from "@vue/reactivity";

export interface Article {
  id: string;
  title: string;
  url: string;
  content: string;
  author: string;
  date: string;
  tags: string[];
  sections: string[];
}

export interface Results {
  results: Article[];
}

const api = inject("api") as AxiosInstance;
async function getItems(
  query: string,
  page: number
): Promise<{ numFound: number; docs: Article[] }> {
  const results = await api.get("/search", {
    params: {
      q: query,
      page: page,
    },
  });
  return results.data;
}

const results = ref([
  {
    id: "",
    title: "",
    url: "",
    content: "",
    author: "",
    date: "",
    tags: [""],
    sections: [""],
  },
]);
const amount = ref(0);
const page = ref(0);
const query = useRoute().query.q as string;
const bottom = ref(false);

watch(bottom, (newValue) => {
  if (newValue) {
    console.log("At the bottom, fetching more items");
    getMoreItems(query);
  }
});

async function getMoreItems(query: string): Promise<void> {
  const newResults = await getItems(query, page.value + 1);
  if (newResults) {
    results.value.push(...newResults.docs);
    page.value++;
  }
}

onMounted(() => {
  window.addEventListener("scroll", () => {
    bottom.value = bottomVisible();
  });
});

const total = computed(() => {
  return amount.value < 8 ? amount.value : (page.value + 1) * 8;
});

const bottomVisible = () => {
  const scrollY = window.scrollY;
  const visible = document.documentElement.clientHeight;
  const pageHeight = document.documentElement.scrollHeight;
  const bottomOfPage = visible + scrollY >= pageHeight;
  return bottomOfPage || pageHeight < visible;
};

onBeforeMount(async () => {
  const items = await getItems(query, 0);
  results.value = items.docs;
  amount.value = items.numFound;
});
</script>

<template>
  <div class="flex pt-20">
    <section class="flex w-1/5 flex-col px-10">
      <h2 class="text-3xl font-sn pb-10">Filters</h2>
      <FilterBox />
    </section>
    <main class="flex flex-col w-3/5 justify-center px-10">
      <p class="self-end">Showing {{ total }} of {{ amount }} results</p>
      <ResultList :results="results" />
      <section></section>
    </main>
    <section class="flex w-1/5 flex-col"></section>
  </div>
</template>
