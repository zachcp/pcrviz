#!/usr/bin/python

import click

@click.command()
@click.option('--width', default=32,)
@click.option('--height', default=32)
@click.option('--copies', default=16)
def run():
    setup()
    make_mol()

def setup(copies=16):
    dnacopies=copies*2
    ## prepare the dna copies. 
    ## change anything about the dna here
    print "##prepare DNA"
    print "load 100bp.pdb"
    print "select dna1, (100bp and chain A)"
    print "select dna2, (100bp and chain B)"
    print "create dna1a, (dna1)"
    print "create dna1b, (dna2)"

    s = range(dnacopies)
    for x in s:
    	if x % 2 == 0:	
    		#molecule1		
    		print "# dna copy %s" % (x)
    		print "create dna%sa, (dna1a)" % (2 + ((x+1)/2)) 
    	else: 
    		#molecule2		
    		print "# dna copy %s" % (x)
    		print "create dna%sb, (dna1b)" % (1 + ((x+1)/2)) 

    print "color wheat, all"
    print "color cerium, elem p"
    print "color bluewhite, elem n"
    print "color boron, elem o"
    print "color white, elem h"
    print "color gray65, elem c"

    print "# Hide nonpolar hydrogens"
    print "select h, elem h "
    print "select hbb, ( elem h and ( name H3* or name H4*) )"
    print "hide lines, h"
    print "hide sticks, h"
    print "hide sphere, h"
    print "show sticks, hbb"
    print "cmd.disable('h')"

    ## prepare the Taq copies. 
    ## change anything about Taq here
    print "#Prepare Polymerase"
    print "load 2KTQ_mod.pdb, 2KTQ"
    print "select taq0,  (2KTQ and chain A)"
    print "create dna1c, (taq0)"
    print "hide sticks, dna1c"
    print "show cartoon, dna1c"
    print "show surface, dna1c"
    print "color copper, dna1c"

    s=range(copies-1)
    for x in s:
    	print"#polymerase copy %s" % (2+x)
    	print "create dna%sc, (dna1c)" % (2+x)

    print "# General style"
    print "hide all"
    print "hide nonbonded"
    print "hide lines"
    print "show sticks, (dna1 or dna2)"
    print "#set sphere_scale=1.1"
    print "set transparency=0.4"
    print "set stick_radius=0.8"
    print "set surface_color,gray50"
    print "set ray_shadows, on"
    print "set ray_shadows, 1"
    print "set ambient,0.20000"
    print "#set spec_reflect,0.4000"
    print "set ray_opaque_background, off"
    print "#set ray_trace_mode,  3"
    print "set orthoscopic, off"
    print "set antialias, 2"
    print "hide sticks, all"


    print "orient dna%sa" % (x+1)		
    #rotation
    s=range(copies)
    for x in s:
    	print "extract test,(dna%sa and resi 101-200)" % (x+1) 
    	print "delete test"
    	print "extract test, (dna%sb and resi 1-100)" % (x+1)
    	print "delete test"
    	print "translate [50,0,0], dna%sc" % (x+1)

    s=range(copies)
    for y in s:
    	if y % 2 != 0:	
    		print "orient dna%sa" % (y+1)				
    		print "rotate [0,1,0], 180, (dna%sa or dna%sb or dna%sc)" % (y+1,y+1,y+1)


    #tranlation
    s = range(copies)
    for z in s:	 
    	if z % 2 == 0:	
    		print "translate [0,%s,0], (dna%sa or dna%sb or dna%sc)" % (90*z,z+1,z+1,z+1)
    		print "show sticks, (dna%sa or dna%sb)" % (z+1,z+1) 
    		print "show cartoon, dna%sc" % (z+1) 		
    		print "show surface, dna%sc" % (z+1)
    	else: 
    		print "translate [0,%s,0], (dna%sa or dna%sb or dna%sc)" % (90*z,z+1,z+1,z+1)
    		print "show sticks, (dna%sa or dna%sb)" % (z+1,z+1) 
    		print "show cartoon, dna%sc" % (z+1) 		
    		print "show surface, dna%sc" % (z+1)		

    #print "reset"
    print "delete (100bp or dna1 or dna2 or h or hbb or taq0 or 2KTQ)"
    print "delete 100bp and 2KTQ"
    #print "rotate [0,1,0], 90, all"
    print "zoom"

def make_mol(frames=370, width=32, height=32):
    #!/usr/bin/python

    print "s = range(370)"
    print "set_view (\
        -0.272705138,    0.031300515,   -0.961589813,\
        -0.937514007,    0.215847954,    0.272903949,\
         0.216098607,    0.975925624,   -0.029517982,\
        -0.000021279,    0.000350142, -1284.348754883,\
      -166.413757324,   69.531135559,  367.137359619,\
       878.178161621, 1690.767944336,    0.000000000 )"
    print "png frame_matrix000.png, width={},height={}".format(width,height)

    s = range(frames)
    for x in s:
    	if x % 2 == 0:	
    		s = range(11)		
    		for y in s:
    			if y % 2 == 0: 
    				print "#molecule %s" % (y+1)
    				print "hide sticks,dna%sa" % (y+1) 
    				print "show sticks, dna%sa and resi 1-%s" % (y+1, 15+x/2)
    				print "orient dna%sa" % (y+1)
    				print "translate [3.14,0,0], dna%sc; rotate x, 18, dna%sc" % (y+1,y+1)		
    			else:				
    				print "#molecule %s" % (y+1)
    				print "hide sticks,dna%sa" % (y+1) 
    				print "show sticks, dna%sa and resi 1-%s" % (y+1, 15+x/2)
    				print "orient dna%sa" % (y+1)
    				print "translate [-3.14,0,0], dna%sc; rotate x, -18, dna%sc" % (y+1,y+1)				
    				print "set_view (\
    				    -0.272705138,    0.031300515,   -0.961589813,\
    				    -0.937514007,    0.215847954,    0.272903949,\
    				     0.216098607,    0.975925624,   -0.029517982,\
    				    -0.000021279,    0.000350142, -1284.348754883,\
    				  -166.413757324,   69.531135559,  367.137359619,\
    				   878.178161621, 1690.767944336,    0.000000000 )"
    				print "png frame_matrix{:03d}.png, width={}, height={}".format( x+1, width, height)  

    	else: 
    		s = range(11)		
    		for y in s:
    			if y % 2 == 0: 
    				print "orient dna%sa" % (y+1)
    				print "rotate x, 18, dna%sc" % (y+1)
    			else:
    				print "orient dna%sa" % (y+1)
    				print "rotate x, -18, dna%sc" % (y+1)
    				print "set_view (\
    				    -0.272705138,    0.031300515,   -0.961589813,\
    				    -0.937514007,    0.215847954,    0.272903949,\
    				     0.216098607,    0.975925624,   -0.029517982,\
    				    -0.000021279,    0.000350142, -1284.348754883,\
    				  -166.413757324,   69.531135559,  367.137359619,\
    				   878.178161621, 1690.767944336,    0.000000000 )"
    				print "png frame_matrix{:03d}.png, width={}, height={}".format( x+1, width, height) 

if __name__ == "__main__":
    run()    
