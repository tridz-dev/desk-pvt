<template>
	<div class="flex flex-col">
		<div class="flex border-b h-[52px] px-[24px] shrink-0">
			<div class="grow my-auto text-[16px] font-semibold text-gray-900">
				Dashboard
			</div>
		</div>
		<TicketTrends />
	</div>
</template>

<script>
import TicketTrends from "@/components/desk/dashboard/TicketTrends.vue"
import TicketSummary from "@/components/desk/dashboard/TicketSummary.vue"
export default {
	name: "Dashboard",
	components: {
		TicketTrends,
		TicketSummary,
	},
}
</script>

<style scoped></style>
