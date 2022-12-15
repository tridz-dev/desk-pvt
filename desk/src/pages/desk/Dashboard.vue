<template>
	<div class="flex flex-col overflow-scroll">
		<div class="flex border-b h-[52px] px-[24px] shrink-0">
			<div class="grow my-auto text-[16px] font-semibold text-gray-900">
				Dashboard
			</div>
		</div>
		<div class="mt-3.5 mr-8 ml-8">Welcome, Fadil</div>
		<TicketStatus />
		<div class="ml-auto w-48 mr-24">
			<Datepicker
				v-model="date"
				range
				@update:modelValue="handleDate"
				:enable-time-picker="false"
			/>
		</div>
		<div class="grid grid-cols-2">
			<TicketTrends class="w-50" />
			<TicketSummary class="w-50" />
			<TicketSummaryTest class="w-50" />
			<TicketType class="w-50" />
		</div>
		<SlaSummary />
	</div>
</template>

<script>
import TicketTrends from "@/components/desk/dashboard/TicketTrends.vue"
import TicketSummary from "@/components/desk/dashboard/TicketSummary.vue"
import TicketType from "@/components/desk/dashboard/TicketType.vue"
import TicketStatus from "@/components/desk/dashboard/TicketStatus.vue"
import TicketSummaryTest from "@/components/desk/dashboard/TicketSummaryTest.vue"
import SlaSummary from "@/components/desk/dashboard/SlaSummary.vue"
import Datepicker from "@vuepic/vue-datepicker"
import "@vuepic/vue-datepicker/dist/main.css"
import { ref } from "vue"
export default {
	name: "Dashboard",
	components: {
		TicketTrends,
		TicketSummary,
		TicketType,
		TicketStatus,
		TicketSummaryTest,
		SlaSummary,
		Datepicker,
	},
	data() {
		return {
			fromDate: "",
			toDate: "",
		}
	},
	setup() {
		let date = ref()
		const handleDate = (modelData) => {
			date.value = modelData
			this.fromDate = new Date(date.value[0]).toLocaleDateString(
				"en-IN",
				{
					year: "numeric",
					month: "2-digit",
					day: "2-digit",
				}
			)

			this.toDate = new Date(date.value[1]).toLocaleDateString("en-IN", {
				year: "numeric",
				month: "2-digit",
				day: "2-digit",
			})
		}

		return {
			date,
			handleDate,
		}
	},
}
</script>

<style scoped></style>
