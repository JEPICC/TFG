import { Box, List, ListItem, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import SingleLineChart from "../components/charts/SingleLineChartWell";
import WellDialog from "../components/WellDialog";

export default function Well() {

  const [meters, setMeters] = useState([]);
  let location = useLocation();
  const well = location.state.well
  const id = well._id;
  const sigla = well.sigla;

  const setting = {
    press: { color: "blue", label: "Presión" },
    temp: { color: "orange", label: "Temperatura" },
    flow: { color: "red", label: "Caudal" },
  };

  const loadMeters = async () => {
    if (id) {
      const response = await fetch("http://localhost:8000/meters/well/" + id);
      const data = await response.json();
      const sorted_data = data.sort((o1, o2) => (o1.tipo > o2.tipo ? 1 : -1));
      setMeters(sorted_data);
    }
  };

  useEffect(() => {
    loadMeters();
  }, [id]);

  return (
    <>
      <Box sx={{ display: 'flex' , alignItems:"center"}}>
        <Typography variant="h4" gutterBottom sx={{ flexGrow:1 }}>
          {sigla}
        </Typography>
        {/* <Button onClick={handleOpen}>Información de pozo</Button> */}
        <WellDialog well={well} />
      </Box>
      
      <List>
        {meters.map((meter) => (
          <ListItem key={meter._id} disablePadding>
            <SingleLineChart
              meter={meter._id}
              label={setting[meter.tipo].label}
              color={setting[meter.tipo].color}
              uom={meter.unidad_medida}
            />
          </ListItem>
        ))}
      </List>
    </>
  );
}
