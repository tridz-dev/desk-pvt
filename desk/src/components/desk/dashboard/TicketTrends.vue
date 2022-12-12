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
					let holder = {}
					res.map((value) => {
						if (
							holder.hasOwnProperty(
								new Date(value.creation).toLocaleDateString(
									"en-US",
									{ year: "2-digit", month: "short" }
								)
							)
						) {
							holder[
								new Date(value.creation).toLocaleDateString(
									"en-US",
									{ year: "2-digit", month: "short" }
								)
							] =
								holder[
									new Date(value.creation).toLocaleDateString(
										"en-US",
										{ year: "2-digit", month: "short" }
									)
								] + value.count
						} else {
							holder[
								new Date(value.creation).toLocaleDateString(
									"en-US",
									{ year: "2-digit", month: "short" }
								)
							] = value.count
						}
						console.log(value)
					})
					console.log("holder", holder)
					var arr = []
					for (var prop in holder) {
						arr.push({ creation: prop, count: holder[prop] })
					}

					arr.map((res) => {
						console.log(res)

						this.ticketCount.push(res.count)
						this.ticketMonth.push(res.creation)
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
