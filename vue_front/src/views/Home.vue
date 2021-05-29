<template>
  <div class="home">
      ホーム
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    //HelloWorld,
  },
};
</script>

<style scoped>
.home{
    @apply hover:text-red-900;
}
</style>
