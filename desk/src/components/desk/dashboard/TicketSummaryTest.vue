<template>
	<v-chart class="chart" :option="option" />
</template>

<script>
import ECharts from "vue-echarts"
import "echarts/lib/chart/bar"

export default {
	name: "TicketSummaryTest",
	components: {
		"v-chart": ECharts,
	},
	props: {
		fromDate: {
			type: String,
			required: true,
		},
		toDate: {
			type: String,
			required: true,
		},
	},
	data() {
		let ticketType = []
		let ticketCount = []
		let testDate = ""
		let option = {
			title: {
				text: "Tickets by Type",
				left: "center",
			},
			yAxis: {
				type: "category",
				data: ticketType,
			},
			xAxis: {
				type: "value",
			},
			series: [
				{
					data: ticketCount,
					type: "bar",
				},
			],
		}

		return {
			option,
			ticketType,
			ticketCount,
			testDate,
		}
	},
	methods: {
		count() {
			this.$resources.getTicketTypeCount.fetch()
		},
	},
	resources: {
		getTicketTypeCount() {
			return {
				method: "frappedesk.api.dashboard.ticket_type",
				params: {
					filters: [
						["creation", "between", ["2022-12-02", "2022-12-14"]],
					],
				},
				onSuccess: (res) => {
					this.testDate = this.fromDate

					console.log(this.testDate, "hgtyui")
					res.map((value) => {
						this.ticketCount.push(value.count)
						this.ticketType.push(value.ticket_type)
					})
				},
				auto: true,
			}
		},
	},
}
</script>
<style scoped>
.chart {
	height: 50vh;
}
</style>
