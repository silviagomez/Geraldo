//larger yellow square//////////////////
difference(){
color("steelblue")
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
	color("steelblue")
	translate([10,0,0])
	cube(size=[1,10,4.8]);

	color("steelblue")
	translate([10,3.5,4.8])
	cube(size=[1,3,1.5]);
	}

color("green") s
translate([9,-.5,1]) 
cube(size=[3,1,2]);

color("green")
translate([9.9,9,1])
cube(size=[2,2,2]);
}

/////sides///////////////////////
difference(){
	union(){
	color("lightgreen")
	translate([0,10,0])
	cube(size=[20,1,10]);

	color("lightgreen")
	translate([0,9,2])
	cube(size=[1,2,2]);

	color("lightgreen")
	translate([10,9,1])
	cube(size=[1,1,2]);
}

color("lightgreen")
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
	color("lightgreen")
	translate([0,-1,0])
	cube(size=[20,1,10]);

	color("lightgreen")
	translate([0,-1,2])
	cube(size=[1,2,2]);

	color("lightgreen")
	translate([10,-.5,1])
	cube(size=[1,1,2]);
	}

color("lightgreen")
translate([0,-1.5,10])
rotate([0,26,0])
cube([23,14,10]);

color("yellowgreen")
translate([2,-1.5,-.1])
cube(size=[3,5,1]);

color("yellowgreen")
translate([11,-1.5,-.1])
cube(size=[3,1.6,1]);
}

//////top thing///////////////////////////////
difference(){
	union() {
	color("skyblue")
	translate([0,-1,10])
	rotate([0,26,0])
	cube([11,12,1]);

	color("skyblue")
	translate([10,0,4.8])
	cube(size=[1,10,1.3]);
	}
color("steelblue")
translate([10,3.5,4.8])
cube(size=[3,3,1.5]);
}

//////base/////////////////////////////////
union(){
color("yellowgreen")
translate([0,-1,-1])
cube(size=[20,12,1]);

translate([0,3.5,0])
color("yellowgreen")
cube(size=[1,3,1]);

color("yellowgreen")
translate([2,10,0])
cube(size=[3,1,1]);

color("yellowgreen")
translate([11,10,0])
cube(size=[3,1,1]);

color("yellowgreen")
translate([2,-1,0])
cube(size=[3,1,1]);

color("yellowgreen")
translate([11,-1,0])
cube(size=[3,1,1]);
}
union(){
color("yellowgreen")
translate([18,3.5,-2])
cube(size=[10,3,1]);

color("yellowgreen")
translate([26,3.5,-3])
cube([2,3,1]);
}


/////////////////wheels (not for printing obviously)//////////////
translate([5,-1,-3])
color("darkolivegreen")
rotate([90,0,0])
cylinder(h=2, r=3.5,$fs=1);


translate([5,13,-3])
color("darkolivegreen")
rotate([90,0,0])
cylinder(h=2, r=3.5,$fs=1);

translate([5,12,-3])
color("darkolivegreen")
rotate([90,0,0])
cylinder(h=14, r=.5);

translate([20,5,-4.3])
color("darkolivegreen")
sphere(r=2,$fs=1);


translate([20,8,-4])
color("darkolivegreen")
rotate([90,0,0])
cylinder(h=6.9, r=.3);

//motors//
color("slategrey")
translate([4,7,-4])
cube([5,3,3]);

color("slategrey")
translate([4,0,-4])
cube([5,3,3]);

color("slategrey")
translate([18,8,-5])
cube([4,1,4]);

color("slategrey")
translate([18,1,-5])
cube([4,1,4]);