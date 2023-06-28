<template>
  <form @submit.prevent="search(query)">
    <div
      class="flex h-11 border-[1.5px] rounded-full border-solid border-snred shadow-none"
    >
      <div class="flex flex-1 pt-1 pr-2 pb-0 pl-3">
        <div class="flex items-center pr-3">
          <div class="m-auto h-5 w-5 leading-5">
            <svg
              focusable="false"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
            >
              <path
                d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"
              ></path>
            </svg>
          </div>
        </div>
        <div class="flex flex-1 flex-wrap">
          <input
            type="text"
            placeholder="To infinity, and beyond!"
            class="bg-transparent border-0 mb-1 p-0 w-full focus:outline-none"
            v-model="query"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps<{ query: string }>();

const query = ref("");

onMounted(() => {
  if (props.query) {
    query.value = props.query;
  }
});

const router = useRouter();
const search = (query: string) => {
  router.push({ name: "search", query: { q: query } });
};
</script>
