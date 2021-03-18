<template>
  <div class="data-table-container">
    <table class="data-table">
      <thead>
        <tr>
          <th
            v-for="column in columns"
            :key="column.key"
            @click="setSortedColumn(column.key)"
          >
            <span>{{ column.name }}</span>
            <span
              v-if="sorting === undefined || sorting.col !== column.key"
              class="sort-icon sort-icon-none"
            >
              <icon name="sort" />
            </span>
            <span
              v-if="currentColumnSorted(column.key, true)"
              class="sort-icon"
            >
              <icon name="sort-ascending" />
            </span>
            <span
              v-if="currentColumnSorted(column.key, false)"
              class="sort-icon"
            >
              <icon name="sort-descending" />
            </span>
          </th>
        </tr>
      </thead>
      <tbody>
        <slot name="body" :items="getPage()" />
      </tbody>
    </table>
    <div class="data-table-footer">
      <div class="data-table-footer-inner">
        <span
          :class="['pagination-ctrl', { disabled: leftPageDisabled }]"
          @click="!leftPageDisabled && changePage(-1)"
        >
          &lt;
        </span>
        <span>
          {{ i18n.t("components.dataTable.pagination", pagination) }}
        </span>
        <span
          :class="['pagination-ctrl', { disabled: rightPageDisabled }]"
          @click="!rightPageDisabled && changePage(1)"
        >
          &gt;
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { useI18n } from "@/plugins/i18n";
import { Icon } from "@/components";

export interface Column {
  key: string;
  name: string;
  sortable?: boolean;
}

export default defineComponent({
  name: "DataTable",
  components: { Icon },
  props: {
    columns: { type: Array as PropType<Column[]>, required: true },
    items: { type: Array as PropType<Record<string, string>[]> },
    perPage: { type: Number, default: 10 },
  },
  setup() {
    const i18n = useI18n();
    return {
      i18n,
    };
  },
  data(): { page: number; sorting?: { col: string; asc: boolean } } {
    return {
      page: 0,
      sorting: undefined,
    };
  },
  computed: {
    pagination(): { start: number; end: number; total: number } {
      const total = (this.items || []).length;
      const start = this.page * this.perPage;
      const end = Math.min(start + this.perPage, total);
      return { start: start + 1, end, total };
    },
    leftPageDisabled(): boolean {
      return this.page <= 0;
    },
    rightPageDisabled(): boolean {
      return this.pagination.end >= this.pagination.total;
    },
  },
  methods: {
    sortItems(items: Record<string, string>[]) {
      if (!this.sorting) return items;
      const key = this.sorting.col;
      const asc = this.sorting.asc ? 1 : -1;
      return [...items].sort((a, b) => (a[key] < b[key] ? -1 * asc : 1 * asc));
    },
    getPage(): unknown[] {
      return this.sortItems(this.items || []).slice(
        this.pagination.start - 1,
        this.pagination.end
      );
    },
    changePage(offset: number): void {
      this.page += offset;
    },
    currentColumnSorted(key: string, ascending: boolean) {
      if (!this.sorting) return false;
      return this.sorting.col === key && this.sorting.asc === ascending;
    },
    setSortedColumn(key: string) {
      if (!this.sorting || this.sorting.col !== key)
        this.sorting = { col: key, asc: true };
      else if (this.sorting.asc) this.sorting.asc = false;
      else this.sorting = undefined;
    },
  },
});
</script>
