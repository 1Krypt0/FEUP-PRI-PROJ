<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import { useRoute } from "vue-router";

const getItems = (query: string) => {
  console.log("query:", query);
  results.value = [
    {
      id: 0,
      title: "Fancy title 0",
      content: "Fancy content of the very lengthy news article 0",
    },
    {
      id: 1,
      title: "Fancy title 1",
      content: "Fancy content of the very lengthy news article 1",
    },
    {
      id: 2,
      title: "Fancy title 2",
      content: "Fancy content of the very lengthy news article 2",
    },
    {
      id: 3,
      title: "Fancy title 3",
      content: "Fancy content of the very lengthy news article 3",
    },
  ];
};

const results = ref([{ id: -1, title: "", content: "" }]);
const query = useRoute().query.q as string;

onBeforeMount(() => {
  getItems(query);
});
</script>

<template>
  <main class="flex items-center justify-center">
    <p>
      We are obviously searching for {{ query }} and we got a bunch of
      {{ results }}
    </p>
  </main>
</template>
