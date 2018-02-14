<template>
  <div class="card">
    <div class="card-header">
        <p class="card-header-title">Add New Wish</p>
    </div>
    <div class="card-content">
        <div class="field">
            <input class="input" type="text" placeholder="Write your wish..." v-model="newWish">
        </div>
    </div>
    <footer class="card-footer">
        <a class="card-footer-item" @click="createWish">Save Wish</a>
    </footer>
  </div>
</template>

<script>
export default {
  name: "CreateWish",
  data() {
    return {
      newWish: ""
    };
  },
  methods: {
    createWish() {
      if (this.newWish.length > 0) {
        const wish = this.newWish;
        const done = false;
        this.$emit("create-wish", {
          wish,
          done
        });
        this.newWish = "";
      }
    }
  }
};
</script>

<style>

</style>
