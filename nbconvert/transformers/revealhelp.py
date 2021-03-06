"""Module that pre-processes the notebook for export via Reveal.
"""
#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from .base import ConfigurableTransformer

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

class RevealHelpTransformer(ConfigurableTransformer):

    def __call__(self, nb, resources):
        """
        Called once to 'transform' contents of the notebook.
        
        Parameters
        ----------
        nb : NotebookNode
            Notebook being converted
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            transformers to pass variables into the Jinja engine.
        """
        
        
        for worksheet in nb.worksheets :
            for i, cell in enumerate(worksheet.cells):
                
                #Make sure the cell has metadata.
                if not cell.get('metadata', None):
                    break
                
                #Get the slide type.  If type is start of subslide or slide,
                #end the last subslide/slide.
                cell.metadata.slide_type = cell.metadata.get('slideshow', {}).get('slide_type', None)
                if cell.metadata.slide_type is None:
                    cell.metadata.slide_type = '-'
                if cell.metadata.slide_type in ['slide']:
                    worksheet.cells[i - 1].metadata.slide_helper = 'slide_end'
                if cell.metadata.slide_type in ['subslide']:
                    worksheet.cells[i - 1].metadata.slide_helper = 'subslide_end'
                    
        return nb, resources
    