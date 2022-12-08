<template>
	<template>
		<div>
			<div ref="chart" style="width: 100%; height: 400px"></div>
		</div>
	</template>
</template>

<script>
import * as echarts from "echarts"

export default {
	name: "TicketTrends",
	props: ["options", "type"],
	data() {
		return {
			chart: null,
			data: [
				{ name: "Point 1", value: 10 },
				{ name: "Point 2", value: 20 },
				{ name: "Point 3", value: 30 },
			],
		}
	},
	mounted() {
		this.loadChart()
	},

	methods: {
		loadChart() {
			this.chart = echarts.init(this.$refs.chart)
			this.fetchData()
		},
		fetchData() {
			console.log(this.data.map((point) => point.name))
			this.chart.setOption({
				xAxis: {
					type: "category",
					data: this.data.map((point) => point.name),
				},
				yAxis: {
					type: "value",
				},
				series: [
					{
						type: "bar",
						data: this.data.map((val) => {
							val.value
						}),
					},
				],
			})
		},
	},
}
</script>
