<template>
  <div class="card" id="card">
      <header class="card-header">
          <p class="card-header-title">{{ keys }}</p>
      </header>
      <div class="card-content" v-show="!isEditing">
          <div class="content">{{ wish.wish }}</div>
      </div>
      <div class="card-content" v-show="isEditing">
          <input class="input" type="text" placeholder="Write your wish..." v-model="wish.wish">
      </div>
      <footer class="card-footer">
          <a class="card-footer-item" v-show="!isEditing && !wish.done" @click="editWish">Edit</a>
          <a class="card-footer-item" v-show="isEditing" @click="editWishDone(keys, wish)">Save</a>
          <a class="card-footer-item" @click="doneWish(keys, wish)" v-show="!isEditing && !wish.done">On Progress</a>
          <a class="card-footer-item" v-show="!isEditing && wish.done">Done</a>
          <a class="card-footer-item" @click="deleteWish(keys)" v-show="!isEditing">Delete</a>
      </footer>
  </div>
</template>

<script>
export default {
  name: "Wish",
  props: ["wish", "keys"],
  data() {
    return {
      isEditing: false
    };
  },
  methods: {
    editWish() {
      this.isEditing = true;
    },
    editWishDone(keys, wish) {
      axios
        .put("http://127.0.0.1:5000/api/wishlist/" + keys, {
          wish: wish.wish,
          done: wish.done
        })
        .then(response => {
          console.log(response.data);
          this.isEditing = false;
        })
        .catch(error => {
          console.log(error);
        });
    },
    doneWish(keys) {
      this.$emit("done-wish", keys);
    },
    deleteWish(keys) {
      this.$emit("delete-wish", keys);
    }
  }
};
</script>

<style>
#card {
  margin-bottom: 2em;
}
</style>
