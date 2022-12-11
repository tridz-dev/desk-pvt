<template>
	<v-chart class="chart" :option="option" />
</template>

<script>
import ECharts from "vue-echarts"
import "echarts/lib/chart/line"
import "echarts/lib/component/polar"

export default {
	components: {
		"v-chart": ECharts,
	},
	data() {
		let ticketCount = []
		let ticketMonth = []
		let option = {
			title: {
				text: "Ticket Trends",
				left: "center",
			},
			tooltip: {
				trigger: "axis",
			},
			xAxis: {
				type: "category",
				data: ticketMonth,
			},
			yAxis: {
				type: "value",
			},
			series: [
				{
					data: ticketCount,
					type: "line",
					showSymbol: false,
					lineStyle: {
						width: 3,
						shadowColor: "rgba(0,0,0,0.3)",
						shadowBlur: 10,
						shadowOffsetY: 8,
					},
				},
			],
		}

		return {
			ticketCount,
			ticketMonth,
			option,
		}
	},

	methods: {
		count() {
			this.$resources.getTicketCount.fetch()
		},
	},
	resources: {
		getTicketCount() {
			return {
				method: "frappedesk.api.dashboard.get_ticket_count",
				onSuccess: (res) => {
					res.map((value) => {
						console.log(value)
						this.ticketCount.push(value.count)
						this.ticketMonth.push(
							new Date(value.opening_date).toLocaleDateString(
								"en-US",
								{ year: "2-digit", month: "short" }
							)
						)
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
