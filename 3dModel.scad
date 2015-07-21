//larger yellow square//////////////////
difference(){
cube(size=[1,10,10]);

translate([-.1,3.5,-2])
color("blue")
cube(size=[2,3,3]);

color("green")
translate([-1,9,2])
cube(size=[3,2,2]);

color("green")
translate([-1,-1,2])
cube(size=[3,2,2]);
}


//smaller yellow square//////////////
difference(){
	union(){
	translate([10,0,0])
	cube(size=[1,10,4.8]);

	translate([10,3.5,4.8])
	cube(size=[1,3,1.5]);
	}

color("green")
translate([9,-.5,1])
cube(size=[3,1,2]);

color("green")
translate([9.9,9,1])
cube(size=[2,2,2]);
}

/////sides///////////////////////
difference(){
	union(){
	color("lavender")
	translate([0,10,0])
	cube(size=[20,1,10]);

	color("lavender")
	translate([0,9,2])
	cube(size=[1,2,2]);

	color("lavender")
	translate([10,9,1])
	cube(size=[1,1,2]);
}

color("hotpink")
translate([0,-1,10])
rotate([0,26,0])
cube([23,13,10]);

color("blue")
translate([2,9.9,-.1])
cube(size=[3,5,1]);

color("blue")
translate([11,9.9,-.1])
cube(size=[3,5,1]);
}
//----///-/-/-/-/--/--/-/-/-/-/-
difference(){
	union(){
	color("lavender")
	translate([0,-1,0])
	cube(size=[20,1,10]);

	color("lavender")
	translate([0,-1,2])
	cube(size=[1,2,2]);

	color("lavender")
	translate([10,-.5,1])
	cube(size=[1,1,2]);
	}

color("hotpink")
translate([0,-1.5,10])
rotate([0,26,0])
cube([23,14,10]);

color("blue")
translate([2,-1.5,-.1])
cube(size=[3,5,1]);

color("blue")
translate([11,-1.5,-.1])
cube(size=[3,1.6,1]);
}

//////top thing///////////////////////////////
difference(){
	union() {
	color("Fuchsia")
	translate([0,-1,10])
	rotate([0,26,0])
	cube([11,12,1]);

	color("Fuchsia")
	translate([9,0,4.8])
	cube(size=[2,10,1.3]);
	}
color("red")
translate([9.9,3.5,4.7])
cube(size=[3,3,1.5]);
}

//////base/////////////////////////////////
union(){
color("blue")
translate([0,-1,-1])
cube(size=[20,12,1]);

translate([0,3.5,0])
color("blue")
cube(size=[1,3,1]);

color("blue")
translate([2,10,0])
cube(size=[3,1,1]);

color("blue")
translate([11,10,0])
cube(size=[3,1,1]);

color("blue")
translate([2,-1,0])
cube(size=[3,1,1]);

color("blue")
translate([11,-1,0])
cube(size=[3,1,1]);
}

