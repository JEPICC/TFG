import { LineChart } from "@mui/x-charts/LineChart";
import { useEffect, useState } from "react";

export default function SingleLineChart2(prop) {

  const [values, setValues] = useState([]);
  const setting = {
    press: { color: "blue", label: "Presión" },
    temp: { color: "orange", label: "Temperatura" },
    flow: { color: "green", label: "Caudal" },
  };

  const customize = {
    height: 300,
    width: 600,
    legend: { hidden: true },
    margin: { top: 5 },
    // stackingOrder: 'descending',
  };


  useEffect(() => {
    fetch("http://localhost:8000/values/meter/" + prop.meter._id)
      .then((response) => response.json())
      .then((data) => {
        const dataPlus = data.map(({ timestamp, value }) => ({
          date: new Date(timestamp).getHours(),
          value: value,
        }));
        setValues(dataPlus);
      });
  }, [prop.meter._id]);

  if (values.length == 0) return "";

  return (
    <LineChart
      xAxis={[
        {
          dataKey: "date",
          valueFormatter: (v) => v.toString(),
        },
      ]}
      series={[
        {
          dataKey: "value",
          label: setting[prop.meter.tipo].label,
          color: setting[prop.meter.tipo].color,
          showMark: false,
        },
      ]}
      dataset={values}
      {...customize}
    />
  );
}
