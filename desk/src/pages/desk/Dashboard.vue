<template>
	<div class="flex flex-col ml-[200px]">
		<div class="flex border-b h-[52px] px-[24px] shrink-0">
			<div class="grow my-auto text-[16px] font-semibold text-gray-900">
				Dashboard
			</div>
		</div>
		<div class="overflow-y-scroll h-full">
			<div class="mt-3.5 mr-8 ml-8">Welcome {{ user }}</div>
			<TicketStatus />
			<div class="ml-auto mr-6 w-48 mb-[20px]">
				<Datepicker
					v-model="date"
					range
					@update:modelValue="handleDate"
					:enable-time-picker="false"
				/>
			</div>
			<div class="grid grid-cols-2">
				<TicketTrends
					class="w-50"
					:fromDate="fromDate"
					:toDate="toDate"
				/>
				<TicketSummaryChart
					class="w-50"
					:fromDate="fromDate"
					:toDate="toDate"
				/>
				<TicketSummaryTest
					class="w-50"
					:fromDate="fromDate"
					:toDate="toDate"
				/>
				<TicketType
					:fromDate="fromDate"
					:toDate="toDate"
					class="w-50"
				/>
			</div>
			<SlaSummary />
		</div>
	</div>
</template>

<script>
import TicketTrends from "@/components/desk/dashboard/TicketTrends.vue"
import TicketSummary from "@/components/desk/dashboard/TicketSummary.vue"
import TicketType from "@/components/desk/dashboard/TicketType.vue"
import TicketStatus from "@/components/desk/dashboard/TicketStatus.vue"
import TicketSummaryTest from "@/components/desk/dashboard/TicketSummaryTest.vue"
import TicketSummaryChart from "@/components/desk/dashboard/TicketSummaryChart.vue"
import SlaSummary from "@/components/desk/dashboard/SlaSummary.vue"
import Datepicker from "@vuepic/vue-datepicker"
import "@vuepic/vue-datepicker/dist/main.css"
import { ref, onMounted } from "vue"
import { auto } from "@popperjs/core"
export default {
	name: "Dashboard",
	components: {
		TicketTrends,
		TicketSummary,
		TicketType,
		TicketStatus,
		TicketSummaryTest,
		SlaSummary,
		TicketSummaryChart,
		Datepicker,
	},

	data() {
		let date = {}
		let fromDate = ""
		let toDate = ""

		return {
			date,
			fromDate,
			toDate,
		}
	},

	computed: {
		user() {
			console.log(this.$resources.sessionUser.data)
		},
	},

	methods: {
		handleDate(modelData) {
			this.date.value = modelData
			this.fromDate = new Date(this.date.value[0]).toLocaleDateString(
				"en-IN",
				{
					year: "numeric",
					month: "2-digit",
					day: "2-digit",
				}
			)
			this.fromDate = this.fromDate.split("/").reverse().join("-")
			this.toDate = new Date(this.date.value[1]).toLocaleDateString(
				"en-IN",
				{
					year: "numeric",
					month: "2-digit",
					day: "2-digit",
				}
			)
			this.toDate = this.toDate.split("/").reverse().join("-")
			console.log(this.fromDate, this.toDate)
			console.log(frappe.session.user)
		},
	},

	beforeMount() {
		const startDate = new Date().setDate(new Date().getDate() - 7)
		const endDate = new Date()
		this.date.value = [startDate, endDate]
		this.fromDate = startDate
		this.fromDate = new Date(startDate).toLocaleDateString("en-IN", {
			year: "numeric",
			month: "2-digit",
			day: "2-digit",
		})
		this.fromDate = this.fromDate.split("/").reverse().join("-")
		this.toDate = endDate
		this.toDate = new Date(endDate).toLocaleDateString("en-IN", {
			year: "numeric",
			month: "2-digit",
			day: "2-digit",
		})
		this.toDate = this.toDate.split("/").reverse().join("-")
	},

	resources: {
		sessionUser() {
			return {
				method: "frappedesk.api.general.get_session_user",
				
				auto: true,
			}
		},
	},

	// setup() {
	// 	onMounted(() => {
	// 		const startDate = new Date().setDate(new Date().getDate() - 7)
	// 		const endDate = new Date()
	// 		this.date.value = [startDate, endDate]
	// 		this.fromDate = startDate
	// 		this.fromDate = new Date(startDate).toLocaleDateString("en-IN", {
	// 			year: "numeric",
	// 			month: "2-digit",
	// 			day: "2-digit",
	// 		})
	// 		this.fromDate = this.fromDate.split("/").reverse().join("-")
	// 		this.toDate = endDate
	// 		this.toDate = new Date(endDate).toLocaleDateString("en-IN", {
	// 			year: "numeric",
	// 			month: "2-digit",
	// 			day: "2-digit",
	// 		})
	// 		this.toDate = this.toDate.split("/").reverse().join("-")
	// 	})
	// },

	// setup() {
	// 	let fromDate = ref("")
	// 	let toDate = ref("")
	// 	let date = ref()

	// 	onMounted(() => {
	// const startDate = new Date()
	// const endDate = new Date(
	// 	new Date().setDate(startDate.getDate() + 7)
	// )
	// date.value = [startDate, endDate]
	// fromDate = startDate
	// toDate = endDate
	// 	})
	// 	const handleDate = (modelData) => {
	// 		date.value = modelData
	// 		fromDate = new Date(date.value[0]).toLocaleDateString("en-IN", {
	// 			year: "numeric",
	// 			month: "2-digit",
	// 			day: "2-digit",
	// 		})

	// 		fromDate = fromDate.split("/").reverse().join("-")

	// 		toDate = new Date(date.value[1]).toLocaleDateString("en-IN", {
	// 			year: "numeric",
	// 			month: "2-digit",
	// 			day: "2-digit",
	// 		})

	// 		toDate = toDate.split("/").reverse().join("-")

	// 		console.log(toDate, "helelelle")
	// 	}

	// 	return {
	// 		fromDate,
	// 		toDate,
	// 		date,
	// 		handleDate,
	// 	}
	// },
}
</script>

<style scoped></style>
