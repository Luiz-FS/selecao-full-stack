import React from "react";
import { Helmet, HelmetProvider } from 'react-helmet-async';
import PropTypes from 'prop-types';

const Page = props => {
    const { title, children, ...rest } = props;

    return (
        <div {...rest}>
            <HelmetProvider>
                <Helmet>
                    <title>{title}</title>
                </Helmet>
                {children}
            </HelmetProvider>
        </div>
    );
};

Page.propTypes = {
    children: PropTypes.node,
    title: PropTypes.string
};

export default Page;
