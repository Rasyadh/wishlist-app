<template>
  <div class="content">
      <wish v-for="(wish, keys) in wishes" :key="keys" :wish.sync="wish" :keys.sync="keys" @done-wish="doneWish" @delete-wish="deleteWish"></wish>
    </div>
</template>

<script>
import Vue from "vue";
import Wish from "./Wish";

export default {
  name: "WishList",
  props: ["wishes"],
  components: {
    Wish
  },
  methods: {
    doneWish(keys) {
      axios
      .put("http://127.0.0.1:5000/api/wishlist/" + keys, {
        wish: this.wishes[keys].wish,
        done: true
      })
      .then(response => {
        console.log(response.data);
        this.wishes[keys].done = true;
      })
      .catch(error => {
        console.log(error);
      })
    },
    deleteWish(keys) {
      axios
        .delete("http://127.0.0.1:5000/api/wishlist/" + keys)
        .then(response => {
          console.log(response);
          Vue.delete(this.wishes, keys);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>

</style>
