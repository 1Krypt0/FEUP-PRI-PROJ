<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import { useRoute } from "vue-router";
import ResultList from "../components/ResultList.vue";

export interface Article {
  title: string;
  url: string;
  content: string;
  author: string;
  date: Date;
  tags: string[];
  sections: string[];
}

export interface Results {
  results: Article[];
}

const getItems = (query: string) => {
  results.value = [
    {
      title: "Fancy title 0",
      content: "Fancy content of the very lengthy news article 0",
      url: "Url 0",
      author: "Author 0",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
    {
      title: "Fancy title 1",
      content: "Fancy content of the very lengthy news article 1",
      url: "Url 1",
      author: "Author 1",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
    {
      title: "Fancy title 2",
      content: "Fancy content of the very lengthy news article 2",
      url: "Url 2",
      author: "Author 2",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
    {
      title: "Fancy title 3",
      content: "Fancy content of the very lengthy news article 3",
      url: "Url 3",
      author: "Author 0",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
  ];
};

const results = ref([
  {
    title: "",
    url: "",
    content: "",
    author: "",
    date: new Date(),
    tags: [""],
    sections: [""],
  },
]);
const query = useRoute().query.q as string;

onBeforeMount(() => {
  getItems(query);
});
</script>

<template>
  <div class="flex pt-20">
    <section class="flex w-1/5 flex-col items-center">
      <h2 class="text-xl font-sn">Filters</h2>
    </section>
    <main class="flex w-3/5 justify-center px-10">
      <ResultList :results="results" />
    </main>
    <section class="flex w-1/5 flex-col"></section>
  </div>
</template>
