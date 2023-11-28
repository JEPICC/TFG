import { List, ListItem } from "@mui/material";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import SingleLineChart from "../components/charts/SingleLineChart";

export default function Well() {
  const [meters, setMeters] = useState([]);
  let location = useLocation();
  const id = location.state.wid;

  const sigla = location.state.sigla;
  const loadMeters = async () => {
    if (id) {
      const response = await fetch("http://localhost:8000/meters/well/" + id);
      const data = await response.json();
      const sorted_data = data.sort((o1, o2) => (o1.tipo > o2.tipo) ? 1 : -1)
      setMeters(sorted_data);
    }
  };

  useEffect(() => {
    loadMeters();
  }, [id]);

  return (
    <>
      <h2>{sigla}</h2>
      <List>
        {meters.map((meter) => (
          <ListItem key={meter._id} disablePadding>
            <SingleLineChart meter={meter}/>
          </ListItem>
        ))}
      </List>
    </>
  );
}
